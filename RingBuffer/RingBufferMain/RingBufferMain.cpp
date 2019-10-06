#include <iostream>
#include "RingBufferHeader.h"
#include <thread>
#include <mutex>
#include <string>
#include <Windows.h>

void PcWrite(RingBuffer* inBuffer, char pcWrite, float sleep) {
	std::cout << "PcWrite() started" << "\n";
	for (;;) {
		inBuffer->PcWrite(pcWrite);
		Sleep(sleep);
	}
}
void HumanWrite(RingBuffer* inBuffer, float sleep) {
	std::cout << "HumanWrite() started" << "\n";
	std::string input;

	for (;;) {
		std::cin >> input;
		for (int i = 0; i <= (int)input.length(); i++) { //for each character in input, humanwrite(nextChar)
			inBuffer->HumanWrite(input[i]);
		}
		Sleep(sleep);
	}
	
}
void Read(RingBuffer* inBuffer,float sleep) {
	std::cout << "Read() started" << "\n";
	for (;;) {
		if (GetKeyState(VK_TAB) & 0x8000) //when tab is pressed print the buffer
		{
			Sleep(sleep);
			std::cout << "\n" <<"Reading Buffer" << std::endl;
			inBuffer->ReadBuffer();
		}
		else {
			Sleep(sleep);
		}
	}
}

void start(int size, float writeSleepTimer, float readSleepTimer) {
	std::cout << "STARTING" << "\n";
	RingBuffer buffer(size);
	#pragma region instantiate threads


	std::thread TPcWrite(PcWrite, &buffer, '*', writeSleepTimer);
	std::thread THumanWrite(HumanWrite,&buffer, writeSleepTimer);
	std::thread TRead(Read,&buffer, readSleepTimer);

	TPcWrite.join();
	THumanWrite.join();
	TRead.join();
	#pragma endregion
}

int main() {
	start(10,400,100);
}
