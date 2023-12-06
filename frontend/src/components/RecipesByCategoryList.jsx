/**
 * RecipesByCategoryList.jsx
 *
 * This file contains the RecipesByCategoryList component, which displays a list of recipes based on a specific category.
 */

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useParams } from 'react-router-dom';

/**
 * RecipesByCategoryList Component
 *
 * Displays a list of recipes based on a specific category. Fetches category information and related recipes from the API.
 *
 * @returns {JSX.Element} JSX representation of the RecipesByCategoryList component
 */
const RecipesByCategoryList = () => {
  const { categoryId } = useParams();
  const [recipes, setRecipes] = useState([]);
  const [categoryName, setCategoryName] = useState('');

  useEffect(() => {
    /**
     * Fetches information about the specified category from the API.
     *
     * @async
     * @function
     * @returns {Promise<void>}
     */
    const fetchCategoryInfo = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/categories/${categoryId}/`);
        setCategoryName(response.data.name);
      } catch (error) {
        console.error('Error fetching category info:', error);
      }
    };

    /**
     * Fetches a list of recipes based on the specified category from the API.
     *
     * @async
     * @function
     * @returns {Promise<void>}
     */
    const fetchRecipes = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/recipes/category/${categoryId}/`);
        setRecipes(response.data);
      } catch (error) {
        console.error('Error fetching recipes by category:', error);
      }
    };

    fetchCategoryInfo();
    fetchRecipes();
  }, [categoryId]);

  if (!recipes.length) {
    return <div>Загрузка...</div>;
  }

  return (
    <div className="container">
      <h2>{`Список рецептов категории: "${categoryName}"`}</h2>
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

export default RecipesByCategoryList;
