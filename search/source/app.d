/*
** Made by Alex Strole, Kenny Le, and Robert Wong for bitclave hackathon.
*/

// Python conversions
import pyd.pyd;

// Types
import std.json         : JSONValue, JSONException;
import std.typecons     : Tuple;

// Functions
import std.json         : parseJSON;
import std.algorithm    : sort;
import std.array        : split;
import std.conv         : to;
import std.string       : strip;

alias product_tuple = Tuple!(ulong, double);
alias option        = Tuple!(int, product_tuple[]);

/*
** Compare string one with string two and get how many characters are
** alike. Then change that to a percentage.
*/
pragma(inline, true);
static double compare_characters(string one,
                                 string two)
{
    double alike;
    ulong maxlength = one.length > two.length ?
                        one.length : two.length;

    alike = 0;
    one = one.strip();
    two = two.strip();
    foreach (i; 0 .. one.length)
        if (i < two.length && one[i] == two[i])
            alike++;
    alike = alike / maxlength;
    if (alike > 0) return (alike);
    else return (0);
}

/*
** Take the item and the input and split them into key words.
** We then take those key words and compare it against all the words in the input.
*/ 
pragma(inline, true);
static double get_alike_percentage(string item,
                                   string input)
{
    double score = 0.0;
    string[] keywords = item.split(" ");
    string[] words = input.split(" ");

    foreach (i; 0 .. words.length)
        foreach (j; 0 .. keywords.length)
                score += compare_characters(words[i], keywords[j]);
    return (score / words.length);
}

/*
** For everything inside a category, get the percentage compared against the input.
*/
static product_tuple[] get_product_scores(JSONValue category,
                                          string input)
{
    product_tuple[] values;
    double percentage;

    foreach (string key, value; category)
    {
        percentage = get_alike_percentage(value["name"].str, input); 
        if (percentage > 0)
            values ~= product_tuple(to!ulong(key), percentage);
    }
    return values;
}

/* 
** Given an input, category, and a json; parse the json
** and go through all the products and compare it to the input.
** Based on how alike they are, give them a score.
**
** Return format: (return code, [(product name, score)])
**
** Error table:
**  0 succeeded
** -1 failed to find category in search
** -2 empty input
** -3 malformed json
*/
extern(C) option search_products(string input,
                                 string[] categories,
                                 string json)
{
    JSONValue parsed_json;
    JSONValue category_json;
    product_tuple[] temp_values;
    product_tuple[] values;

    try
        parsed_json = parseJSON(json);
    catch (JSONException)
        return option(-3, null);

    if (input == "")
        return option(-2, null);    

    // If they inputted categories, then only check those categories.
    // If they did not input a category, just go over all the products
    if (categories.length > 0)
    {
        foreach (category; categories)
        {
            try
                category_json = parsed_json[category];
            catch(JSONException)
                return option(-1, null);    
            temp_values = get_product_scores(category_json, input);
            foreach (product; temp_values)
                values ~= product;
        }
    }
    else
        foreach (string key, value; parsed_json)
        {
            temp_values = get_product_scores(value, input);
            foreach (product; temp_values)
                values ~= product;
        }
    values.sort!((x, y) => x[1] > y[1]);
    return option(0, values);
}

/*
** Export functions to python
*/
extern(C) void PydMain() {
    def!(search_products)();
    module_init();
}
