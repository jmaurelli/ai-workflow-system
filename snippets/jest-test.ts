import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { {{componentName}} } from './{{componentName}}';

describe('{{componentName}}', () => {
  const defaultProps = {
    // Add your default props here
  };

  beforeEach(() => {
    // Setup before each test
  });

  afterEach(() => {
    // Cleanup after each test
    jest.clearAllMocks();
  });

  it('should render correctly', () => {
    render(<{{componentName}} {...defaultProps} />);
    
    // Add your assertions here
    expect(screen.getByRole('button')).toBeInTheDocument();
  });

  it('should handle user interactions', async () => {
    render(<{{componentName}} {...defaultProps} />);
    
    const button = screen.getByRole('button');
    fireEvent.click(button);
    
    await waitFor(() => {
      // Add your assertions here
      expect(screen.getByText('Updated text')).toBeInTheDocument();
    });
  });

  it('should handle errors gracefully', () => {
    // Mock console.error to avoid noise in tests
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
    
    render(<{{componentName}} {...defaultProps} />);
    
    // Add your error handling test here
    
    consoleSpy.mockRestore();
  });

  describe('when {{condition}}', () => {
    it('should {{expectedBehavior}}', () => {
      render(<{{componentName}} {...defaultProps} />);
      
      // Add your conditional test here
    });
  });
}); 