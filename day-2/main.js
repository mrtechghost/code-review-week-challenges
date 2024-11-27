const express = require('express');
const app = express();

app.get('/search', (req, res) => {
  let searchTerm = req.query.term;

  // Ha, good luck popping an alert now!
  searchTerm = searchTerm.replace(/alert/i, '').replace(/src/i, '');

  res.send(`<h1>Search results for: ${searchTerm}</h1>`);
});

app.listen(3000, () => console.log('App running on port 3000'));
