class Solution {
    public String longestPalindrome(String s) {
        String updatedS = getUpdated(s); // make lps array on updated string 
        int lps[] = new int[updatedS.length()];
        int c = 0; // centre 
        int r = 0; // radius 
        for(int i = 1;i<updatedS.length()-1;i++){
            int mirror  = c-(i-c); // coordinates of mirror image , look at the mirror image and get a kickstart 
            if(i<r){
                lps[i] = Math.min(lps[mirror],r-i); // taking min because we are bounded by the fact that we have processed only certain part of the string 
            }
            while(updatedS.charAt(i+lps[i]+1)==updatedS.charAt(i-lps[i]-1)) lps[i]++; // checking if extremes are equal if yes then increment lps[i] 
            if(i+lps[i]>r){ // update radius and centre if greater radius found 
                r = i+lps[i];
                c  = i;
            }
        }
        int maxLen = Integer.MIN_VALUE;
        int maxIdx = -1;
        for(int i =0;i<lps.length;i++) { // get length of longest palindromic substring 
            int val = lps[i];
            if(lps[i]>maxLen){ 
                maxLen = lps[i];
                maxIdx = i;
            }
        }
        int firstIdx = maxIdx-maxLen+1;
        int actIdx = (firstIdx-2)/2; // getting index of first character of longest palindromic substring based on observation 
        return s.substring(actIdx,actIdx+maxLen);
    }
    public String getUpdated(String s){ // function to make updated string 
        StringBuilder sb = new StringBuilder();
        sb.append("@");
        for(char ch : s.toCharArray()){
            sb.append("#");
            sb.append(ch);
        }
        sb.append("#");
        sb.append("$");
        return sb.toString();
    }
}
