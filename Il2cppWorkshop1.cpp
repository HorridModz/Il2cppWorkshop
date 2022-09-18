#include <limits> // don't delete!
#include <iostream>
#include <filesystem>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <string.h>


#ifdef WINDOWS
#include <direct.h>
#define getcwd _getcwd
#else
#include <unistd.h>
#endif

//Function to pause and wait for user input before continuing
void waitforchar(bool finished = false) {
	if (finished) {
		std::cout << "Program finished. Enter anything to continue";
	} else {
		std::cout << "Program paused. Enter anything to continue";
	}
	//std::cin.clear(); // reset any error flags
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // ignore any characters in the input buffer until we find an enter character
	std::cin.get(); // get one more char from the user
}
//Trimming whitespace from string functions
//Thanks to https://stackoverflow.com/questions/216823/how-to-trim-a-stdstring

// trim from start
static inline std::string &ltrim(std::string &s) {
    s.erase(s.begin(), std::find_if(s.begin(), s.end(),
            std::not1(std::ptr_fun<int, int>(std::isspace))));
    return s;
}

// trim from end
static inline std::string &rtrim(std::string &s) {
    s.erase(std::find_if(s.rbegin(), s.rend(),
            std::not1(std::ptr_fun<int, int>(std::isspace))).base(), s.end());
    return s;
}

// trim from both ends
static inline std::string &trim(std::string &s) {
    return ltrim(rtrim(s));
}
	
//Function to convert string to dictionary
//Thanks to https://stackoverflow.com/questions/38812780/split-string-into-key-value-pairs-using-c
	std::map<std::string, std::string> stringtodict(std::string const& s)
{
    std::map<std::string, std::string> m;

    std::string key, newkey, val, newval;
    std::istringstream iss(s);
    while(std::getline(std::getline(iss, key, ':') >> std::ws, val))
		newkey = key.erase(0,key.find("\""));
		newkey = trim(newkey);
		/*
		if (val.find("\"") < val.back()) {
			if (val.find(":") < val.find("\"")) {
				newval = val.erase(0,val.find("\""));
			} else {
				newval = val;
			}
		} else {
			if (val.find(":") < val.back()) {
				newval = val.erase(0,val.find(":"));
			} else {
				newval = val;
			}
		}
		*/
		val = trim(val);
		if (val.back() == ',') {
			newval = val.substr(0,val.length() - 1);
		} else {
			newval = val;
		}
		newval = trim(newval);
        m[newkey] = newval;

    return m;
}

//Function to run the Il2cppWorkshop.py script
void runpython() {
	std::cout << "Loading setup.json file..." << std::endl;
	//Get the current directory and store it in currentdir
	//Then convert it to a std::string
	char currentdirchar[FILENAME_MAX];
	getcwd(currentdirchar,FILENAME_MAX);
	std::string currentdir = currentdirchar;
	//Load the contents of the setup.json file into fullsetup
	std::string fullsetupstring;
	std::string setuppath = currentdir + "/setup.json";
	std::ifstream setupfile; 
	setupfile.open(setuppath);
	if (not(setupfile.good())) {
			std::cout << "Could not open setup.json. Check that this file exists in the path '" << setuppath << "' and that it is not currently in use by any other programs." << std::endl;
			waitforchar(true);
			exit(1);
	}
	while (setupfile.good()){
		fullsetupstring += setupfile.get();
	}
	std::cout << "Parsing setup.json file..." << std::endl;
	//Convert fullsetup from std::string to char*
	char* fullsetup = const_cast<char*>(fullsetupstring.c_str());
	//Parse the setup.json file and get the python interpreter path
	auto setup = stringtodict(fullsetup);
	if (setup.find("\"python interpreter path\"") == setup.end()) {
	std::cout << "Could not find python interpreter path in setup.json file" << std::endl;
	waitforchar(true);
	exit(1);
	}
	std::string pythonpath = setup["\"python interpreter path\""];
	std::cout << "Got python interpreter path from setup.json file: " << pythonpath << std::endl;
	std::cout << "Running Il2cppWorkshop.py..." << std::endl;
	//Get the file path of the python script and the python interpreter
	std::string pythonscriptname = "Il2cppWorkshop.py";
	std::string pythonscriptpath = currentdir + "/" + pythonscriptname;
	//Build the command, then run it
	std::string command = pythonpath + " " + pythonscriptpath;
	system(command.c_str());
}

void runbatch(){
	std::cout << "Running Il2cppWorkshop.py..." << std::endl;
	std::string command = "py Il2cppWorkshop.py\necho Finished running\npause";
	system(command.c_str());
}

int main() {
	runbatch();
	waitforchar(true); // don't delete!
	return 0;
}
