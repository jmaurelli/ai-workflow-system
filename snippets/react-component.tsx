import React from 'react';

interface {{componentName}}Props {
  // Add your props here
  children?: React.ReactNode;
}

export const {{componentName}}: React.FC<{{componentName}}Props> = ({ 
  children,
  ...props 
}) => {
  return (
    <div {...props}>
      {children}
    </div>
  );
};

export default {{componentName}}; 