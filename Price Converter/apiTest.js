const axios = require('axios');

const requestOptions = {
  method: 'GET',
  headers: {
    'apikey': 'uSXHgASsK7em0buawdfZzY1xo6OWqQLX'
  }
};

axios.get('https://api.apilayer.com/currency_data/live', requestOptions)
  .then(response => console.log(response.data))
  .catch(error => console.log('Request failed', error));