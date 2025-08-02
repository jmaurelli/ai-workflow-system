# Firebase Workflow Documentation

## Overview

This document outlines the complete Firebase deployment workflow for SuelenClean, including setup, configuration, deployment, and maintenance procedures. Firebase provides hosting, database, and authentication services for our Next.js application.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Configuration](#configuration)
4. [Deployment Workflow](#deployment-workflow)
5. [Environment Management](#environment-management)
6. [Monitoring & Maintenance](#monitoring--maintenance)
7. [Troubleshooting](#troubleshooting)
8. [Security Best Practices](#security-best-practices)

---

## Prerequisites

### Required Tools
- **Node.js** (v18 or higher)
- **npm** or **yarn**
- **Firebase CLI** (v12 or higher)
- **Git** for version control

### Firebase CLI Installation
```bash
# Install Firebase CLI globally
npm install -g firebase-tools

# Verify installation
firebase --version

# Login to Firebase
firebase login
```

### Project Dependencies
Ensure these are installed in your project:
```bash
npm install firebase
npm install -D firebase-tools
```

---

## Initial Setup

### 1. Firebase Project Creation

1. **Create Firebase Project**:
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Click "Add project"
   - Name: `suelenclean` (or your preferred name)
   - Enable Google Analytics (recommended)
   - Choose analytics account or create new

2. **Enable Services**:
   - **Hosting**: For web deployment
   - **Firestore**: For database (future use)
   - **Authentication**: For user management (future use)
   - **Storage**: For file uploads (future use)

### 2. Local Firebase Configuration

```bash
# Initialize Firebase in your project
firebase init

# Select services:
# ✅ Hosting: Configure files for Firebase Hosting
# ✅ Firestore: Configure security rules and indexes
# ✅ Functions: Configure a Cloud Functions directory (optional)

# Configure Hosting:
# - Public directory: out
# - Single-page app: Yes
# - Overwrite index.html: No

# Configure Firestore:
# - Rules file: firestore.rules
# - Indexes file: firestore.indexes.json
```

### 3. Environment Variables Setup

Create `.env.local` for local development:
```bash
# Firebase Configuration
NEXT_PUBLIC_FIREBASE_API_KEY=your_api_key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
NEXT_PUBLIC_FIREBASE_APP_ID=your_app_id

# Email Service (Resend)
RESEND_API_KEY=your_resend_api_key
```

Create `.env.production` for production:
```bash
# Production Firebase Configuration
NEXT_PUBLIC_FIREBASE_API_KEY=your_production_api_key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
NEXT_PUBLIC_FIREBASE_APP_ID=your_app_id

# Production Email Service
RESEND_API_KEY=your_production_resend_api_key
```

---

## Configuration

### 1. Firebase Configuration Files

#### `firebase.json` (Current Configuration)
```json
{
  "hosting": {
    "public": "out",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ],
    "headers": [
      {
        "source": "**/*.@(js|css)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      },
      {
        "source": "**/*.@(jpg|jpeg|gif|png|svg|webp|ico)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      }
    ]
  }
}
```

#### `firestore.rules` (For Future Database)
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow read access to all users
    match /{document=**} {
      allow read: if true;
      allow write: if false; // Restrict writes for now
    }
  }
}
```

#### `firestore.indexes.json` (For Future Database)
```json
{
  "indexes": [],
  "fieldOverrides": []
}
```

### 2. Next.js Configuration

#### `next.config.js` (Current Configuration)
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Required for static export
  trailingSlash: true, // Required for Firebase hosting
  images: {
    unoptimized: true, // Required for static export
    domains: ['firebasestorage.googleapis.com'],
    formats: ['image/webp', 'image/avif'],
  },
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin',
          },
        ],
      },
    ]
  },
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true,
      },
    ]
  },
}

module.exports = nextConfig
```

### 3. Package.json Scripts

Add these scripts to your `package.json`:
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit",
    "export": "next build && next export",
    "deploy": "npm run build && firebase deploy",
    "deploy:hosting": "npm run build && firebase deploy --only hosting",
    "firebase:login": "firebase login",
    "firebase:logout": "firebase logout",
    "firebase:use": "firebase use",
    "firebase:projects": "firebase projects:list"
  }
}
```

---

## Deployment Workflow

### 1. Pre-Deployment Checklist

Before deploying, ensure:
- [ ] All tests pass (`npm test`)
- [ ] Linting passes (`npm run lint`)
- [ ] Type checking passes (`npm run type-check`)
- [ ] Environment variables are set
- [ ] Firebase project is selected
- [ ] You're on the correct Git branch

### 2. Development Deployment

```bash
# 1. Build the application
npm run build

# 2. Deploy to Firebase
firebase deploy

# Or use the combined script
npm run deploy
```

### 3. Production Deployment

```bash
# 1. Switch to production environment
firebase use production

# 2. Set production environment variables
export $(cat .env.production | xargs)

# 3. Build and deploy
npm run deploy

# 4. Verify deployment
firebase hosting:channel:list
```

### 4. Staging Deployment

```bash
# 1. Create staging channel
firebase hosting:channel:create staging

# 2. Deploy to staging
firebase deploy --only hosting --channel staging

# 3. Get staging URL
firebase hosting:channel:list
```

### 5. Automated Deployment (CI/CD)

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Firebase

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Run linting
      run: npm run lint
    
    - name: Build application
      run: npm run build
      env:
        NEXT_PUBLIC_FIREBASE_API_KEY: ${{ secrets.FIREBASE_API_KEY }}
        NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN: ${{ secrets.FIREBASE_AUTH_DOMAIN }}
        NEXT_PUBLIC_FIREBASE_PROJECT_ID: ${{ secrets.FIREBASE_PROJECT_ID }}
        NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET: ${{ secrets.FIREBASE_STORAGE_BUCKET }}
        NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID: ${{ secrets.FIREBASE_MESSAGING_SENDER_ID }}
        NEXT_PUBLIC_FIREBASE_APP_ID: ${{ secrets.FIREBASE_APP_ID }}
        RESEND_API_KEY: ${{ secrets.RESEND_API_KEY }}
    
    - name: Deploy to Firebase
      uses: FirebaseExtended/action-hosting-deploy@v0
      with:
        repoToken: '${{ secrets.GITHUB_TOKEN }}'
        firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
        channelId: live
        projectId: your-project-id
```

---

## Environment Management

### 1. Environment Variables

#### Development (`.env.local`)
```bash
# Firebase Configuration
NEXT_PUBLIC_FIREBASE_API_KEY=your_dev_api_key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=suelenclean-dev.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=suelenclean-dev
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=suelenclean-dev.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456789
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456789:web:abcdef123456

# Email Service
RESEND_API_KEY=your_dev_resend_key
```

#### Production (`.env.production`)
```bash
# Firebase Configuration
NEXT_PUBLIC_FIREBASE_API_KEY=your_prod_api_key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=suelenclean.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=suelenclean
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=suelenclean.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456789
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456789:web:abcdef123456

# Email Service
RESEND_API_KEY=your_prod_resend_key
```

### 2. Firebase Project Management

```bash
# List all projects
firebase projects:list

# Switch between projects
firebase use suelenclean-dev    # Development
firebase use suelenclean        # Production

# Check current project
firebase use
```

### 3. Environment-Specific Deployments

```bash
# Development deployment
firebase use suelenclean-dev
npm run deploy

# Production deployment
firebase use suelenclean
npm run deploy
```

---

## Monitoring & Maintenance

### 1. Performance Monitoring

#### Firebase Analytics
- Monitor user engagement
- Track page performance
- Analyze user behavior

#### Core Web Vitals
- Monitor LCP, FID, CLS
- Set up alerts for performance issues
- Regular performance audits

### 2. Error Monitoring

#### Firebase Crashlytics (Future)
```bash
# Install Crashlytics
npm install @firebase/crashlytics

# Initialize in your app
import { getCrashlytics } from 'firebase/crashlytics';
```

#### Custom Error Tracking
```javascript
// In your error boundary or error handler
const logError = (error, errorInfo) => {
  console.error('Error:', error);
  // Send to your preferred error tracking service
};
```

### 3. Regular Maintenance Tasks

#### Weekly
- [ ] Check Firebase Console for errors
- [ ] Review analytics data
- [ ] Monitor performance metrics
- [ ] Update dependencies if needed

#### Monthly
- [ ] Security audit
- [ ] Performance optimization review
- [ ] Backup verification
- [ ] Cost analysis

#### Quarterly
- [ ] Full security review
- [ ] Architecture review
- [ ] Dependency updates
- [ ] Feature planning

### 4. Backup Strategy

#### Code Backup
```bash
# Ensure code is backed up to Git
git push origin main

# Create release tags
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

#### Database Backup (Future)
```bash
# Export Firestore data
firebase firestore:export ./backups/firestore-$(date +%Y%m%d)

# Import Firestore data
firebase firestore:import ./backups/firestore-20231201
```

---

## Troubleshooting

### 1. Common Deployment Issues

#### Build Failures
```bash
# Clear Next.js cache
rm -rf .next
npm run build

# Check for TypeScript errors
npm run type-check

# Verify environment variables
echo $NEXT_PUBLIC_FIREBASE_API_KEY
```

#### Firebase CLI Issues
```bash
# Re-authenticate
firebase logout
firebase login

# Clear Firebase cache
firebase use --clear

# Check Firebase CLI version
firebase --version
```

#### Hosting Issues
```bash
# Check hosting configuration
firebase hosting:channel:list

# View hosting logs
firebase hosting:log

# Clear hosting cache
firebase hosting:clear
```

### 2. Performance Issues

#### Slow Loading
- Check image optimization
- Verify caching headers
- Monitor bundle size
- Use Firebase CDN effectively

#### Build Time Issues
- Optimize dependencies
- Use Next.js build cache
- Consider incremental builds

### 3. Environment Variable Issues

```bash
# Verify environment variables are loaded
npm run build 2>&1 | grep -i "NEXT_PUBLIC"

# Check for missing variables
node -e "console.log(process.env.NEXT_PUBLIC_FIREBASE_API_KEY)"
```

---

## Security Best Practices

### 1. Environment Variables
- Never commit `.env` files to Git
- Use different API keys for dev/prod
- Rotate keys regularly
- Use Firebase App Check (future)

### 2. Firebase Security Rules
```javascript
// Example Firestore security rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Restrict access based on authentication
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Public read-only data
    match /public/{document=**} {
      allow read: if true;
      allow write: if false;
    }
  }
}
```

### 3. HTTPS Enforcement
```json
// In firebase.json
{
  "hosting": {
    "headers": [
      {
        "source": "**",
        "headers": [
          {
            "key": "Strict-Transport-Security",
            "value": "max-age=31536000; includeSubDomains"
          }
        ]
      }
    ]
  }
}
```

### 4. Content Security Policy
```javascript
// In next.config.js
async headers() {
  return [
    {
      source: '/(.*)',
      headers: [
        {
          key: 'Content-Security-Policy',
          value: "default-src 'self'; script-src 'self' 'unsafe-eval' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"
        }
      ]
    }
  ]
}
```

---

## Advanced Features (Future)

### 1. Custom Domain Setup
```bash
# Add custom domain
firebase hosting:sites:add your-domain.com

# Configure DNS
# Add CNAME record pointing to your-project.web.app
```

### 2. A/B Testing
```bash
# Create experiment
firebase hosting:channel:create experiment-a

# Deploy variant
firebase deploy --only hosting --channel experiment-a
```

### 3. Edge Functions
```javascript
// functions/index.js
const functions = require('firebase-functions');

exports.api = functions.https.onRequest((req, res) => {
  // Your API logic here
});
```

---

## Conclusion

This Firebase workflow provides a robust foundation for deploying and maintaining your SuelenClean application. Key points to remember:

1. **Always test locally** before deploying
2. **Use environment-specific configurations**
3. **Monitor performance and errors regularly**
4. **Keep security rules updated**
5. **Maintain regular backups**
6. **Follow the deployment checklist**

For additional support:
- [Firebase Documentation](https://firebase.google.com/docs)
- [Next.js Documentation](https://nextjs.org/docs)
- [Firebase Console](https://console.firebase.google.com/)

---

## Quick Reference Commands

```bash
# Development
npm run dev                    # Start development server
npm run build                 # Build for production
npm run deploy               # Build and deploy

# Firebase
firebase login               # Login to Firebase
firebase use                 # Check current project
firebase deploy              # Deploy all services
firebase deploy --only hosting  # Deploy only hosting

# Monitoring
firebase hosting:channel:list  # List hosting channels
firebase hosting:log          # View hosting logs
firebase projects:list        # List all projects
``` 