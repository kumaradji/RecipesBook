/**
 * App.js
 *
 * This file contains the main application component that sets up the routing
 * and navigation for the recipe app.
 */

import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import Categories from './components/Categories';
import RecipesList from './components/RecipesList';
import RecipeDetail from './components/RecipeDetail';
import SwaggerComponent from './components/SwaggerComponent';
import RecipesByCategoryList from './components/RecipesByCategoryList';
import './styles/App.css';

/**
 * App Component
 *
 * The main component that defines the structure and routing of the application.
 * It uses React Router for navigation.
 *
 * @returns {JSX.Element} JSX representation of the App component
 */
const App = () => {
  return (
    <Router>
      {/* Navigation Bar */}
      <nav className="navbar">
        <NavLink to="/" className="nav-link" activeClassName="active-link">
          Категории
        </NavLink>
        <NavLink to="/recipes" className="nav-link" activeClassName="active-link">
          Рецепты
        </NavLink>
        <NavLink to="/swagger" className="nav-link" activeClassName="active-link">
          Swagger
        </NavLink>
      </nav>

      {/* Route Configuration */}
      <Routes>
        <Route path="/recipes" element={<RecipesList />} />
        <Route path="/recipes/:id" element={<RecipeDetail />} />
        <Route
          path="/categories/:categoryId"
          element={<RecipesByCategoryList />}
        />
        <Route path="/swagger" element={<SwaggerComponent />} />
        <Route path="/" element={<Categories />} />
      </Routes>
    </Router>
  );
};

export default App;
