var createError = require('http-errors');
var express = require('express');
var path = require('path');


var app = express();

const port = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));


// catch 404 and forward to error handler
app.use(function (req, res) {
    res.status(404)
    res.render('error', { title: 'Not Found', logged: false, error: createError(404) })
});

// error handler
app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
});

module.exports = app;

app.listen(port, ()=> console.log("Client on port " + port));