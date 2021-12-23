// basic file operations
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


int countNumberOfIncreases(ifstream& myfile){
	myfile.open("input1.txt");
	string line;
	int prev = -1;
	int ans = 0;
	if (myfile.is_open()){

		while ( getline(myfile,line)){
			int x = atoi(line.c_str());

			if (prev >= 0 && x > prev){
				ans = ans + 1;
			}
			prev = x;
		}
		myfile.close();
	}

	return ans;
}


int slideWindowIncrement(ifstream& myfile){

	myfile.open("input1.txt");
	string line;
	int prev = -1;
	int ans  = 0;
	vector<int> data;
	while (getline(myfile, line)){
		int x = atoi(line.c_str());
		data.push_back(x);
	}


	for (int i=0; i<data.size();i=i+1){
		int cur = data[i] + data[i+1] + data[i+2];
		if (prev >= 0 && cur > prev){
			ans = ans + 1;
		}
		prev = cur;

	}
	return ans;
	
}


int main() {
	ifstream myfile;
	int ans1 = countNumberOfIncreases(myfile);
	int ans2 = slideWindowIncrement(myfile);
	cout << "" << ans2;


}
