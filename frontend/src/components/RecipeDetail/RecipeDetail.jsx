/**
 * RecipeDetail.jsx
 *
 * This file contains the RecipeDetail component, which displays detailed information about a specific recipe.
 */

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

/**
 * RecipeDetail Component
 *
 * Displays detailed information about a specific recipe, fetched from the API based on the provided recipe ID.
 *
 * @returns {JSX.Element} JSX representation of the RecipeDetail component
 */
const RecipeDetail = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    /**
     * Fetches detailed information about the recipe from the API.
     *
     * @async
     * @function
     * @returns {Promise<void>}
     */
    const fetchRecipeData = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/recipes/${id}/`);
        setRecipe(response.data);
      } catch (error) {
        console.error('Error fetching recipe data:', error);
      }
    };

    fetchRecipeData();
  }, [id]);

  if (!recipe) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container">
      <h2>{recipe.title}</h2>
      <p>{recipe.content}</p>
    </div>
  );
};

export default RecipeDetail;
