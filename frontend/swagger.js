import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";

const App = () => <SwaggerUI url="http://127.0.0.1:8000/Recipes/swagger.json" />;

export default App;
