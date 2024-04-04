class Solution {
    public int maxDepth(String s) {
        Stack<Character> stack = new Stack<>();
        char[] ch = s.toCharArray();
        int maxLevel = 0;
        for (char c: ch){
            if (c == '(') stack.add(c);
            else if (c == ')') stack.pop();
            int size = stack.size();
            maxLevel = Math.max(maxLevel, size);
        }
        return maxLevel;
    }
}