#include "RingBufferHeader.h"
#include <iostream>


#pragma region Constructors


RingBuffer::RingBuffer() {
	bufferSize = 10;
	bufferCharArray = new char[bufferSize];
}
RingBuffer::RingBuffer(int size) {
	bufferSize = size;
	bufferCharArray = new char[bufferSize];
}


#pragma endregion


void RingBuffer::PcWrite(char input) {

	std::unique_lock<std::mutex> PcWriteLock(PcMutex); 
	/*LOCKED*/
	if (input != NULL) {
	bufferCharArray[inputIndex] = input; //insert character into the designated location in the array
	inputIndex = (inputIndex+1) % getBufferSize(); //increase inputindex inbetween 0 <-> bufferSize
	std::cout << input; //print the character written by the computer
	}
	/*UNLOCKED*/
	PcWriteLock.unlock();
}

void RingBuffer::HumanWrite(char input) {
	std::unique_lock<std::mutex> HumanWriteLock(HumanMutex);
	/*LOCKED*/
	if (input != NULL) {
		bufferCharArray[inputIndex] = input;
		inputIndex = (inputIndex + 1) % getBufferSize();
		std::cout << input;
	}
	/*UNLOCKED*/
	HumanWriteLock.unlock();
}


void RingBuffer::ReadBuffer() {
	std::unique_lock<std::mutex> HumanWriteLock(HumanMutex);
	std::unique_lock<std::mutex> PcWriteLock(PcMutex);
	std::unique_lock<std::mutex> ReadLock(ReadMutex);
	//lock everything as the only process we want running is the print of the ringbuffer
	for(int i = 0; i <= bufferSize; i++) {
		std::cout << outputIndex << " : " << bufferCharArray[i] << "\n";
	}
	HumanWriteLock.unlock();
	PcWriteLock.unlock();
	ReadLock.unlock();
}
