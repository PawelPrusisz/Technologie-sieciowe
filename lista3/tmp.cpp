std::string encode(std::string text) {
	int oneCount = 0;
	std::stringstream output;

	for (size_t i = 0; i < text.length(); i++) {
		if (text[i] == '1') {
			oneCount++;
		}
		else {
			oneCount = 0;
		}

		if (oneCount == 5) {
			output << text[i] << "0";
			oneCount = 0;
		}
		else {
			output << text[i];
		}
	}

	return output.str();
}

std::string decode(std::string text) {
	int oneCount = 0;
	std::stringstream output;

	for (size_t i = 0; i < text.length(); i++) {
		if (text[i] == '1') {
			oneCount++;
		}
		else {
			oneCount = 0;
		}

		if (oneCount == 5) {
			output << text[i];
			i++; // next char is '0'. This should be ignored
			oneCount = 0;
		}
		else {
			output << text[i];
		}
	}

	return output.str();
}

std::string getCRC(std::string source) {
	std::uint32_t crc = CRC::Calculate(source.c_str(), source.length(), CRC::CRC_32());

	std::string hex;
	std::stringstream ss;
	ss << std::hex << crc;
	unsigned n;
	ss >> n;
	std::bitset<32> b(n);

	return b.to_string();
}