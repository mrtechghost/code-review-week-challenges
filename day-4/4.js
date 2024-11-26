const express = require('express');
const app = express();

app.use((req, res, next) => {
  res.setHeader("Content-Security-Policy", "script-src 'self' https://*.google.com");
  next();
});

app.get('/search', (req, res) => {
  let searchTerm = req.query.term;
  console.log("The term is: " + searchTerm)
  searchTerm = searchTerm.replace(/<script>.*?<\/script>/gi, '');
  console.log("The filtered term is: " + searchTerm)

  res.send(`<h1>Search results for: ${searchTerm}</h1>`);
});

app.listen(3000, () => console.log('App running on port 3000'));
