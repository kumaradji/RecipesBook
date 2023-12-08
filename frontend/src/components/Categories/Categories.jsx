/**
 * Categories.js
 *
 * This file contains the Categories component, which displays a list of recipe categories.
 * Users can click on a category to view recipes belonging to that category.
 */

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

/**
 * Categories Component
 *
 * Displays a list of recipe categories and allows users to navigate to recipes within a specific category.
 *
 * @returns {JSX.Element} JSX representation of the Categories component
 */
const Categories = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    /**
     * Fetches the list of recipe categories from the API.
     *
     * @async
     * @function
     * @returns {Promise<void>}
     */
    const fetchCategories = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/categories/');
        setCategories(response.data);
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    fetchCategories();
  }, []);

  return (
    <div>
      <h2>Выберете рецепты блюд из категории</h2>
      <ul>
        {categories.map(category => (
          <li key={category.id}>
            <Link to={`/categories/${category.id}`}>{category.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Categories;
