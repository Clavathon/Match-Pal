import pyd.pyd;
import std.stdio;
import std.json;
import std.conv;

extern(C) string[] search_products(string input, string json)
{
	JSONValue parsed_json = parseJSON(json);
	writeln(parsed_json["Computers"]);
	return null;
}

extern(C) void PydMain() {
    def!(search_products)();
    module_init();
}

