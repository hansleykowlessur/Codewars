String.prototype.toJadenCase = function () {
    /*
    Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
    Jaden is also known for some of his philosophy that he delivers via Twitter. 
    When writing on Twitter, he is known for almost always capitalizing every word. 
    For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

    Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

    Example:
    Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
    Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
    */
   
    // Get original text
    let originalText = this.toString();

    // Converted sentence
    let result;

try {
    // Split each word from the sentence
    let eachWord = originalText.split(" ");

    /* 
       1. Loop over each word
       2. Convert first character of each word to uppercase
       3. Join converted word to form the output as required
    */

    result = eachWord
        .map((word) => {
            // Convert first character to uppercase and concatenate the remaining characters
            return word[0].toUpperCase() + word.substring(1);
        })
        .join(" ");
    } 
    finally {
        return result;
    }
};
