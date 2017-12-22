#!/usr/bin/env node --harmony

var program = require('commander'),
  request = require('request');

program
  .arguments('<slng>')
  .action((slng) => {
    var options = {
      method: 'GET',
      url: 'http://api.urbandictionary.com/v0/define',
      qs: {
        term: slng
      },
      headers: {
        'Cache-Control': 'no-cache',
        Accept: 'application/json'
      }
    }

    request(options, function (err, res, body) {
      if (err) throw new Error(err);
      var trimRes;
      var results = JSON.parse(body).list;
      if (results.length > 3) {
        trimRes = results.slice(0, 3);
      } else {
        trimRes = results;
      }
      trimRes.forEach((result, index) => {
        if (typeof (result.definition) !== undefined) {
          var i = index+1;
          console.log("=======================\n" + i + ": " + result.definition);
        }
      });
    });
  })
  .parse(process.argv);