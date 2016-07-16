// If we execute this Javascript, what will the browser's console show?

var text = 'outside';
function logIt(){
    console.log(text);
    var text = 'inside';
};
logIt();

// Hoisting. In Javascript, variable declarations are "hoisted" to the top of 
// the current scope. Variable assignments, however, are not.
// The declaration (but not the assignment) of text gets hoisted to the top of 
// logIt(). So our code gets interpreted as though it were:

var text = 'outside';
function logIt(){
    var text;
    console.log(text);
    text = 'inside';
};
logIt();

// So we have a new variable text inside of logIt() that is initialized to 
// undefined, which is what it holds when we hit our log statement.
