class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        if (deck == null || deck.length == 0) {
            return deck;
        }

        Arrays.sort(deck);
        if (deck.length == 2) {
            return deck;
        }

        Deque<Integer> queue = new LinkedList<>();
        for (int i = deck.length - 1; i >= 0; --i) {
            if (deck.length - i <= 2) {
                queue.addLast(deck[i]);
                continue;
            }

            queue.addLast(queue.pollFirst());
            queue.addLast(deck[i]);
        }

        int[] res = new int[queue.size()];
        int i = 0;
        while (!queue.isEmpty()) {
            int value = queue.pollLast();
            res[i++] = value;
        }

        return res;
    }
}