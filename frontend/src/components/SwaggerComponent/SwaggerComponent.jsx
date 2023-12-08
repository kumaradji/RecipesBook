/**
 * SwaggerComponent.jsx
 *
 * This file contains the SwaggerComponent, which renders the Swagger UI for API documentation.
 */

import React from 'react';
import SwaggerUI from 'swagger-ui-react';
import 'swagger-ui-react/swagger-ui.css';

/**
 * SwaggerComponent
 *
 * Renders the Swagger UI for API documentation.
 *
 * @returns {JSX.Element} JSX representation of the SwaggerComponent
 */
const SwaggerComponent = () => {
  const swaggerUrl = 'http://127.0.0.1:8000/swagger.json';

  return (
    <div>
      <SwaggerUI url={swaggerUrl} />
    </div>
  );
};

export default SwaggerComponent;
