class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = '';
        for (let s of strs) {
            result += `${s.length}x${s}`;
        }
        return result;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let result = [];
        let i = 0;

        while (i < str.length) {
            let j = i;
            while (str[j] !== 'x') {
                j++;
            }
            let length = parseInt(str.substring(i, j), 10);
            result.push(str.substring(j+1, j+1+length));
            i = j = j+1+length;
        }
        return result;
    }
}
