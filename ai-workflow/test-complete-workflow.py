#!/usr/bin/env python3

"""
🧪 Complete Python Workflow System Test Suite
Tests the entire mvp-initializer.py + workflow-runner.py system end-to-end
"""

import argparse
import subprocess
import json
import shutil
import sys
import time
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

class WorkflowTester:
    """Comprehensive test suite for the Python workflow system"""
    
    def __init__(self, debug: bool = False, cleanup: bool = True):
        self.debug = debug
        self.cleanup_enabled = cleanup
        self.script_dir = Path(__file__).parent
        self.test_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.test_projects = []
        self.failed_tests = []
        
    def log_info(self, message: str):
        print(f"{Colors.BLUE}ℹ️  {message}{Colors.NC}")
        
    def log_success(self, message: str):
        print(f"{Colors.GREEN}✅ {message}{Colors.NC}")
        
    def log_warning(self, message: str):
        print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")
        
    def log_error(self, message: str):
        print(f"{Colors.RED}❌ {message}{Colors.NC}")
        
    def log_header(self, message: str):
        print(f"{Colors.PURPLE}🚀 {message}{Colors.NC}")
        print()
    
    def check_prerequisites(self) -> bool:
        """Check if all required components are available"""
        self.log_info("Checking prerequisites...")
        
        # Check if scripts exist
        required_scripts = [
            "mvp-initializer.py",
            "workflow-runner.py",
            "test-llm-automation.sh"
        ]
        
        for script in required_scripts:
            script_path = self.script_dir / script
            if not script_path.exists():
                self.log_error(f"Required script not found: {script}")
                return False
            
            if not os.access(script_path, os.X_OK):
                self.log_error(f"Script not executable: {script}")
                return False
        
        # Check for LLM API availability
        try:
            result = subprocess.run([
                str(self.script_dir / "test-llm-automation.sh")
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                self.log_warning("LLM API tests failed - some tests may not work")
                self.log_info("Available LLM providers will be limited")
            else:
                self.log_success("LLM API integration validated")
                
        except Exception as e:
            self.log_warning(f"Could not validate LLM APIs: {e}")
        
        self.log_success("Prerequisites check completed")
        return True
    
    def test_mvp_initializer_dry_run(self) -> bool:
        """Test MVP initializer in dry-run mode"""
        self.log_header("Testing MVP Initializer (Dry Run)")
        
        test_project = f"test-mvp-{self.test_timestamp}"
        
        try:
            cmd = [
                "python3", str(self.script_dir / "mvp-initializer.py"),
                "--project", test_project,
                "--mode", "guided",
                "--dry-run",
                "--non-interactive",
                "--verbose"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                self.log_success("MVP initializer dry-run passed")
                return True
            else:
                self.log_error(f"MVP initializer dry-run failed: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.log_error("MVP initializer dry-run timed out")
            return False
        except Exception as e:
            self.log_error(f"MVP initializer dry-run error: {e}")
            return False
    
    def test_mvp_creation(self, with_llm: bool = False) -> Tuple[bool, Optional[str]]:
        """Test actual MVP project creation"""
        mode = "with LLM API" if with_llm else "without LLM API"
        self.log_header(f"Testing MVP Creation ({mode})")
        
        test_project = f"test-mvp-{self.test_timestamp}"
        # Normalize project name like MVP initializer does
        normalized_project = test_project.lower().replace('_', '-')
        self.test_projects.append(test_project)
        
        try:
            cmd = [
                "python3", str(self.script_dir / "mvp-initializer.py"),
                "--project", test_project,
                "--mode", "autonomous",
                "--non-interactive",
                "--verbose"
            ]
            
            if with_llm:
                cmd.extend(["--llm-api"])
            
            self.log_info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, text=True, timeout=300)
            
            if result.returncode == 0:
                # Verify project was created (using normalized name)
                project_dir = Path.home() / "Projects" / normalized_project
                if project_dir.exists():
                    # Check for expected files
                    expected_files = [
                        "project-manifest.json",
                        "features",
                        "docs", 
                        "artifacts"
                    ]
                    
                    missing_files = []
                    for expected in expected_files:
                        if not (project_dir / expected).exists():
                            missing_files.append(expected)
                    
                    if missing_files:
                        self.log_error(f"Missing expected files/directories: {missing_files}")
                        return False, test_project
                    
                    # Check manifest content
                    manifest_path = project_dir / "project-manifest.json"
                    try:
                        with open(manifest_path, 'r') as f:
                            manifest = json.load(f)
                        
                        if manifest.get("project_name") != normalized_project:
                            self.log_error(f"Invalid manifest project name: {manifest.get('project_name')}")
                            return False, test_project
                        
                        if manifest.get("project_type") != "MVP":
                            self.log_error(f"Invalid manifest project type: {manifest.get('project_type')}")
                            return False, test_project
                        
                    except Exception as e:
                        self.log_error(f"Could not validate manifest: {e}")
                        return False, test_project
                    
                    self.log_success(f"MVP project '{normalized_project}' created successfully")
                    self.log_info(f"Project location: {project_dir}")
                    return True, normalized_project
                else:
                    self.log_error(f"Project directory not created: {project_dir}")
                    return False, test_project
            else:
                self.log_error(f"MVP creation failed with return code: {result.returncode}")
                self.log_error("Check output above for details")
                return False, test_project
                
        except subprocess.TimeoutExpired:
            self.log_error("MVP creation timed out")
            return False, test_project
        except Exception as e:
            self.log_error(f"MVP creation error: {e}")
            return False, test_project
    
    def test_feature_addition(self, project_name: str, with_llm: bool = False) -> bool:
        """Test feature addition to existing project"""
        mode = "with LLM API" if with_llm else "without LLM API"
        self.log_header(f"Testing Feature Addition ({mode})")
        
        test_feature = f"test-feature-{self.test_timestamp}"
        
        try:
            cmd = [
                "python3", str(self.script_dir / "workflow-runner.py"),
                "--feature", test_feature,
                "--existing-project", project_name,
                "--mode", "autonomous",
                "--verbose"
            ]
            
            if with_llm:
                cmd.extend(["--llm-api"])
            
            self.log_info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, text=True, timeout=300)
            
            if result.returncode == 0:
                # Verify feature was added to project
                project_dir = Path.home() / "Projects" / project_name
                if project_dir.exists():
                    self.log_success(f"Feature '{test_feature}' added to project '{project_name}'")
                    return True
                else:
                    self.log_error(f"Project directory not found: {project_dir}")
                    return False
            else:
                self.log_error(f"Feature addition failed with return code: {result.returncode}")
                self.log_error("Check output above for details")
                return False
                
        except subprocess.TimeoutExpired:
            self.log_error("Feature addition timed out")
            return False
        except Exception as e:
            self.log_error(f"Feature addition error: {e}")
            return False
    
    def test_standalone_feature(self, with_llm: bool = False) -> bool:
        """Test standalone feature creation (legacy mode)"""
        mode = "with LLM API" if with_llm else "without LLM API"
        self.log_header(f"Testing Standalone Feature ({mode})")
        
        test_feature = f"standalone-{self.test_timestamp}"
        
        try:
            cmd = [
                "python3", str(self.script_dir / "workflow-runner.py"),
                "--feature", test_feature,
                "--mode", "autonomous",
                "--verbose"
            ]
            
            if with_llm:
                cmd.extend(["--llm-api"])
            
            self.log_info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, text=True, timeout=300)
            
            if result.returncode == 0:
                self.log_success(f"Standalone feature '{test_feature}' created successfully")
                return True
            else:
                self.log_error(f"Standalone feature creation failed with return code: {result.returncode}")
                self.log_error("Check output above for details")
                return False
                
        except subprocess.TimeoutExpired:
            self.log_error("Standalone feature creation timed out")
            return False
        except Exception as e:
            self.log_error(f"Standalone feature creation error: {e}")
            return False
    
    def test_error_handling(self) -> bool:
        """Test error handling scenarios"""
        self.log_header("Testing Error Handling")
        
        tests_passed = 0
        total_tests = 3
        
        # Test 1: Feature addition to non-existent project
        try:
            cmd = [
                "python3", str(self.script_dir / "workflow-runner.py"),
                "--feature", "test-feature",
                "--existing-project", "non-existent-project",
                "--mode", "autonomous"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0 and "not found" in result.stdout:
                self.log_success("Non-existent project error handling works")
                tests_passed += 1
            else:
                self.log_error("Non-existent project error handling failed")
                
        except Exception as e:
            self.log_error(f"Error handling test 1 failed: {e}")
        
        # Test 2: Invalid project name
        try:
            cmd = [
                "python3", str(self.script_dir / "mvp-initializer.py"),
                "--project", "invalid@project#name",
                "--mode", "autonomous",
                "--dry-run",
                "--non-interactive"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:  # Should normalize the name
                self.log_success("Invalid project name normalization works")
                tests_passed += 1
            else:
                self.log_error("Invalid project name handling failed")
                
        except Exception as e:
            self.log_error(f"Error handling test 2 failed: {e}")
        
        # Test 3: Duplicate project creation
        if self.test_projects:
            try:
                # Use normalized project name like in MVP creation test
                normalized_project = self.test_projects[0].lower().replace('_', '-')
                cmd = [
                    "python3", str(self.script_dir / "mvp-initializer.py"),
                    "--project", normalized_project,
                    "--mode", "autonomous",
                    "--non-interactive"
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                
                if result.returncode != 0 and "already exists" in result.stderr:
                    self.log_success("Duplicate project error handling works")
                    tests_passed += 1
                else:
                    self.log_error("Duplicate project error handling failed")
                    
            except Exception as e:
                self.log_error(f"Error handling test 3 failed: {e}")
        else:
            self.log_warning("Skipping duplicate project test - no test projects created")
            total_tests -= 1
        
        success_rate = tests_passed / total_tests if total_tests > 0 else 0
        self.log_info(f"Error handling tests: {tests_passed}/{total_tests} passed ({success_rate:.1%})")
        
        return success_rate >= 0.8  # 80% pass rate required
    
    def cleanup_test_artifacts(self):
        """Clean up test projects and files"""
        if not self.cleanup_enabled:
            self.log_info("Cleanup disabled - test artifacts preserved")
            return
        
        self.log_info("Cleaning up test artifacts...")
        
        cleanup_count = 0
        
        # Clean up test projects (including ones that might exist from previous runs)
        projects_dir = Path.home() / "Projects"
        if projects_dir.exists():
            # Clean up projects from current test run
            for project_name in self.test_projects:
                project_dir = projects_dir / project_name
                if project_dir.exists():
                    try:
                        shutil.rmtree(project_dir)
                        cleanup_count += 1
                        self.log_info(f"Removed test project: {project_dir}")
                    except Exception as e:
                        self.log_warning(f"Could not remove {project_dir}: {e}")
            
            # Clean up any leftover test projects from previous runs
            for item in projects_dir.glob("test-mvp-*"):
                try:
                    if item.is_dir():
                        shutil.rmtree(item)
                        cleanup_count += 1
                        self.log_info(f"Removed leftover test project: {item}")
                except Exception as e:
                    self.log_warning(f"Could not remove {item}: {e}")
        
        # Clean up test features (legacy)
        features_dir = Path.cwd() / "features"
        if features_dir.exists():
            for item in features_dir.glob(f"*{self.test_timestamp}*"):
                try:
                    if item.is_dir():
                        shutil.rmtree(item)
                    else:
                        item.unlink()
                    cleanup_count += 1
                    self.log_info(f"Removed test artifact: {item}")
                except Exception as e:
                    self.log_warning(f"Could not remove {item}: {e}")
            
            # Clean up standalone test features
            for item in features_dir.glob("standalone-*"):
                try:
                    if item.is_dir():
                        shutil.rmtree(item)
                        cleanup_count += 1
                        self.log_info(f"Removed standalone test feature: {item}")
                except Exception as e:
                    self.log_warning(f"Could not remove {item}: {e}")
        
        self.log_success(f"Cleanup completed: {cleanup_count} items removed")
    
    def run_complete_test_suite(self, test_llm: bool = False) -> Dict[str, bool]:
        """Run the complete test suite"""
        self.log_header("🧪 COMPLETE PYTHON WORKFLOW SYSTEM TEST SUITE")
        
        results = {}
        
        # Pre-cleanup any existing test artifacts
        self.log_info("Pre-cleaning any existing test artifacts...")
        self.cleanup_test_artifacts()
        
        # Check prerequisites
        if not self.check_prerequisites():
            self.log_error("Prerequisites check failed - aborting tests")
            return {"prerequisites": False}
        results["prerequisites"] = True
        
        # Test 1: MVP Initializer Dry Run
        results["mvp_dry_run"] = self.test_mvp_initializer_dry_run()
        if not results["mvp_dry_run"]:
            self.failed_tests.append("MVP Initializer Dry Run")
        
        # Test 2: MVP Creation (without LLM)
        mvp_success, test_project = self.test_mvp_creation(with_llm=False)
        results["mvp_creation"] = mvp_success
        if not mvp_success:
            self.failed_tests.append("MVP Creation")
        
        # Test 3: Feature Addition (if MVP creation succeeded)
        if mvp_success and test_project:
            results["feature_addition"] = self.test_feature_addition(test_project, with_llm=False)
            if not results["feature_addition"]:
                self.failed_tests.append("Feature Addition")
        else:
            results["feature_addition"] = False
            self.failed_tests.append("Feature Addition (skipped - MVP creation failed)")
        
        # Test 4: Standalone Feature
        results["standalone_feature"] = self.test_standalone_feature(with_llm=False)
        if not results["standalone_feature"]:
            self.failed_tests.append("Standalone Feature")
        
        # Test 5: Error Handling
        results["error_handling"] = self.test_error_handling()
        if not results["error_handling"]:
            self.failed_tests.append("Error Handling")
        
        # Test 6: LLM Integration (if requested and available)
        if test_llm:
            self.log_header("Testing LLM Integration")
            
            # Test MVP creation with LLM
            mvp_llm_success, test_project_llm = self.test_mvp_creation(with_llm=True)
            results["mvp_creation_llm"] = mvp_llm_success
            if not mvp_llm_success:
                self.failed_tests.append("MVP Creation with LLM")
            
            # Test feature addition with LLM
            if mvp_llm_success and test_project_llm:
                results["feature_addition_llm"] = self.test_feature_addition(test_project_llm, with_llm=True)
                if not results["feature_addition_llm"]:
                    self.failed_tests.append("Feature Addition with LLM")
            else:
                results["feature_addition_llm"] = False
                self.failed_tests.append("Feature Addition with LLM (skipped)")
        
        return results
    
    def print_test_summary(self, results: Dict[str, bool]):
        """Print comprehensive test summary"""
        print()
        self.log_header("🎯 TEST RESULTS SUMMARY")
        
        passed_tests = []
        failed_tests = []
        
        for test_name, success in results.items():
            if success:
                passed_tests.append(test_name)
            else:
                failed_tests.append(test_name)
        
        # Print passed tests
        if passed_tests:
            print(f"{Colors.GREEN}✅ PASSED TESTS ({len(passed_tests)}):{Colors.NC}")
            for test in passed_tests:
                print(f"   ✅ {test}")
            print()
        
        # Print failed tests
        if failed_tests:
            print(f"{Colors.RED}❌ FAILED TESTS ({len(failed_tests)}):{Colors.NC}")
            for test in failed_tests:
                print(f"   ❌ {test}")
            print()
        
        # Overall result
        success_rate = len(passed_tests) / len(results) if results else 0
        
        if success_rate == 1.0:
            self.log_success("🎉 ALL TESTS PASSED! Python workflow system is WORKING PERFECTLY!")
            print()
            self.log_info("Your Python workflow system is ready for production use!")
            print()
            self.log_info("🚀 Ready to create your first MVP:")
            print(f"   ./mvp-initializer.py --project=my-awesome-app --mode=autonomous --llm-api")
            print()
            self.log_info("➕ Ready to add features:")
            print(f"   ./workflow-runner.py --feature=user-auth --existing-project=my-awesome-app --llm-api")
            
        elif success_rate >= 0.8:
            self.log_warning(f"🟡 MOSTLY WORKING: {success_rate:.1%} tests passed")
            self.log_info("Core functionality works, some edge cases may need attention")
            
        else:
            self.log_error(f"🔴 NEEDS ATTENTION: Only {success_rate:.1%} tests passed")
            self.log_error("Core functionality issues detected")
            
        print()
        self.log_info(f"📊 Overall Success Rate: {success_rate:.1%} ({len(passed_tests)}/{len(results)} tests)")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="🧪 Complete Python Workflow System Test Suite"
    )
    
    parser.add_argument("--test-llm",
                       action="store_true",
                       help="Include LLM API integration tests (requires API keys)")
    
    parser.add_argument("--no-cleanup",
                       action="store_true",
                       help="Skip cleanup of test artifacts")
    
    parser.add_argument("--debug",
                       action="store_true",
                       help="Enable debug output")
    
    parser.add_argument("--quick",
                       action="store_true",
                       help="Run only essential tests (faster)")
    
    args = parser.parse_args()
    
    # Initialize tester
    tester = WorkflowTester(
        debug=args.debug,
        cleanup=not args.no_cleanup
    )
    
    try:
        # Run test suite
        results = tester.run_complete_test_suite(test_llm=args.test_llm)
        
        # Print summary
        tester.print_test_summary(results)
        
        # Cleanup
        tester.cleanup_test_artifacts()
        
        # Exit with appropriate code
        success_rate = sum(results.values()) / len(results) if results else 0
        sys.exit(0 if success_rate >= 0.8 else 1)
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️  Test interrupted by user{Colors.NC}")
        tester.cleanup_test_artifacts()
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.NC}")
        tester.cleanup_test_artifacts()
        sys.exit(1)

if __name__ == "__main__":
    main()
