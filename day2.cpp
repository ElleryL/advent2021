// basic file operations
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class Movement{
	public:
		string dir;
		int dis;

};



int positionMultipler(vector<Movement> movements){
	int depth = 0;
	int horizontal = 0;

	for (Movement movement : movements){

		if (movement.dir == "forward"){
			horizontal = horizontal + movement.dis;
		} else if (movement.dir == "up"){
			depth = depth - movement.dis;
		} else {
			depth = depth + movement.dis;
		}
	}

	return depth * horizontal;
}


int aimedPositionMultipler(vector<Movement> movements){
	int depth = 0;
	int horizontal = 0;
	int aim = 0;
	for (Movement movement : movements){

		if (movement.dir == "forward"){
			horizontal = horizontal + movement.dis;
			depth = depth + aim * movement.dis;
		} else if (movement.dir == "up"){
			aim = aim - movement.dis;
		} else {
			aim = aim + movement.dis;
		}
	}

	return depth * horizontal;


}

int main(){

	ifstream myfile;
	string line;
	vector<Movement> movements;
	myfile.open("input2.txt");
	while (getline(myfile, line)){
		Movement movement;
		int pos = line.find(" ");
		movement.dir = line.substr(0,pos);
		movement.dis = stoi(line.substr(pos+1,line.length()));
		movements.push_back(movement);
	}


	myfile.close();
	int ans1 = positionMultipler(movements);
	int ans2 = aimedPositionMultipler(movements);
	cout << ans2 << "\n";
	return 0;
}