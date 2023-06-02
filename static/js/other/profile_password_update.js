



// for disabling duplicate + sign
// let count = 0



$("#phone").keypress(function(event) {

    let phone_number = $("#phone").val();

    var character = String.fromCharCode(event.keyCode);
    let valid = isValid(character);
    
    
    if (character == "+" && phone_number.length > 0) {
        return false;
    }

    return valid;
    
});

function isValid(str) {
    return !/[~`!#$%\^&*()@_qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM.=\-\[\]\\';,/{}|\\":<>\?]/g.test(str);
}