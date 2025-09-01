module.exports = {
  // Print width
  printWidth: 80,
  
  // Tab width
  tabWidth: 2,
  
  // Use spaces instead of tabs
  useTabs: false,
  
  // Semicolons at the end of statements
  semi: true,
  
  // Use single quotes instead of double quotes
  singleQuote: true,
  
  // Quote props only when necessary
  quoteProps: 'as-needed',
  
  // Use double quotes in JSX
  jsxSingleQuote: false,
  
  // Add trailing commas where valid in ES5
  trailingComma: 'es5',
  
  // Spaces inside object literal braces
  bracketSpacing: true,
  
  // Put the > of a multi-line JSX element at the end of the last line
  bracketSameLine: false,
  
  // Include parentheses around a sole arrow function parameter
  arrowParens: 'avoid',
  
  // Format only files that have a pragma comment
  requirePragma: false,
  
  // Insert pragma at the top of the file
  insertPragma: false,
  
  // Wrap prose if it exceeds the print width
  proseWrap: 'preserve',
  
  // Respect HTML whitespace sensitivity
  htmlWhitespaceSensitivity: 'css',
  
  // Line endings
  endOfLine: 'lf',
  
  // Embedded language format
  embeddedLanguageFormatting: 'auto',
  
  // Override default options for specific files
  overrides: [
    {
      files: '*.json',
      options: {
        printWidth: 100,
      },
    },
    {
      files: '*.md',
      options: {
        printWidth: 100,
        proseWrap: 'always',
      },
    },
    {
      files: '*.yml',
      options: {
        singleQuote: false,
      },
    },
    {
      files: '*.yaml',
      options: {
        singleQuote: false,
      },
    },
  ],
}; 