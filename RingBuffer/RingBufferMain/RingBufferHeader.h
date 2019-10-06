#pragma once
#include <mutex>
#include <stdlib.h>
#include <Windows.h>
#include <cstdlib>

class RingBuffer
{
private:
	int inputIndex = 0;
	int outputIndex = 0;

public:
	char* bufferCharArray;
	int bufferSize;

	const int getInputIndex() { return inputIndex; }
	const int getOutputIndex() { return outputIndex; }
	const int getBufferSize() { return bufferSize; }

	RingBuffer();
	RingBuffer(int size);

	void PcWrite(char input);
	void HumanWrite(char input);
	
	void ReadBuffer();

	
	std::mutex PcMutex;
	std::mutex HumanMutex;
	std::mutex ReadMutex;


};