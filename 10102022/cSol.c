char * breakPalindrome(char * palindrome){
    if (strlen(palindrome) == 1) {
        return "";
    }
    for (int i = 0; i < floor(strlen(palindrome) / 2); i++) {
        if (palindrome[i] != 'a') {
            palindrome[i] = 'a';
            return palindrome;
        }
    }
    palindrome[strlen(palindrome)-1] = 'b';
    return palindrome;
}
