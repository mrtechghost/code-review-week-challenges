const express = require('express');
const path = require('path');
const app = express();

app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

app.use((req, res, next) => {
  res.setHeader("Content-Security-Policy", "script-src 'self'");
  next();
});

app.get('/search', (req, res) => {
  let searchTerm = req.query.term;
  res.render('search', { searchTerm });
});

app.listen(3000, () => console.log('App running on port 3000'));
