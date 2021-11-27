function filter_list(l) {
    //In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

    // List with filtered items
    let filteredList;

    try {
        // Filter out strings by taking into account only elements which are of Datatype number
        filteredList = l.filter( e => {
            return (typeof e === "number")
        });
    } finally{
         // Return a new array with the strings filtered out
        return filteredList;
    }
}
