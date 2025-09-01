import { Request, Response, NextFunction } from 'express';

interface {{routeName}}Request extends Request {
  // Add your custom request properties here
}

interface {{routeName}}Response extends Response {
  // Add your custom response properties here
}

/**
 * {{routeDescription}}
 * @route {{method}} {{routePath}}
 * @access {{accessLevel}}
 */
export const {{routeName}} = async (
  req: {{routeName}}Request,
  res: {{routeName}}Response,
  next: NextFunction
): Promise<void> => {
  try {
    // Add your route logic here
    
    res.status(200).json({
      success: true,
      message: '{{routeName}} completed successfully',
      data: {
        // Add your response data here
      },
    });
  } catch (error) {
    next(error);
  }
}; 