// Copyright (C) 2023 Joe Baker (JoeBlakeB)
// Advent of Code 2015 - Day 04: The Ideal Stocking Stuffer
// Usage:
//     scripts/cppRun.sh 2015/04-The-Ideal-Stocking-Stuffer.cpp < 2015/inputs/04.txt

#include <iostream>
#include <openssl/evp.h>
#include <openssl/md5.h>
#include <string>

std::string md5(std::string message) {
    EVP_MD_CTX *mdctx;
    unsigned char *md5_digest;
    unsigned int md5_digest_len = EVP_MD_size(EVP_md5());

    // MD5_Init
    mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, EVP_md5(), NULL);

    // MD5_Update
    EVP_DigestUpdate(mdctx, (unsigned char *)message.c_str(), message.length());

    // MD5_Final
    md5_digest = (unsigned char *)OPENSSL_malloc(md5_digest_len);
    EVP_DigestFinal_ex(mdctx, md5_digest, &md5_digest_len);
    EVP_MD_CTX_free(mdctx);

    std::string md5_str;
    char tmp[3];
    for (unsigned int i = 0; i < 3; i++) {
        sprintf(tmp, "%02x", md5_digest[i]);
        md5_str += tmp;
    }

    OPENSSL_free(md5_digest);
    return md5_str;
}

int main() {
    std::string input;
    std::string combined;
    std::string digest;
    std::cin >> input;
    int i = 0;
    bool fiveDigitsNotFound = true;

    while (true) {
        combined = input + std::to_string(++i);
        digest = md5(combined);

        if (digest == "000000") {
            std::cout << "Six zeroes: " << i << std::endl;
            return 0;
        }

        digest.pop_back();
        if (fiveDigitsNotFound && digest == "00000") {
            std::cout << "Five zeroes: " << i << std::endl;
            fiveDigitsNotFound = false;
        }
    }

    return 1;
}