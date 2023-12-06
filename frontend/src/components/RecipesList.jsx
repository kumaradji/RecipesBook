/**
 * RecipesList.jsx
 *
 * This file contains the RecipesList component, which displays a list of all recipes.
 */

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

/**
 * RecipesList Component
 *
 * Displays a list of all recipes fetched from the API.
 *
 * @returns {JSX.Element} JSX representation of the RecipesList component
 */
const RecipesList = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    /**
     * Fetches a list of all recipes from the API.
     *
     * @async
     * @function
     * @returns {Promise<void>}
     */
    const fetchRecipes = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/recipes/');
        setRecipes(response.data);
      } catch (error) {
        console.error('Error fetching recipes:', error);
      }
    };

    fetchRecipes();
  }, []);

  return (
    <div>
      <h2>Список рецептов всех блюд</h2>
      <ul>
        {recipes.map(recipe => (
          <li key={recipe.id}>
            <Link to={`/recipes/${recipe.id}`}>{recipe.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecipesList;
