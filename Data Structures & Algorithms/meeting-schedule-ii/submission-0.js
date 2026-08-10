/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    minMeetingRooms(intervals) {
        const time = new Array(1001).fill(0);
        for(let i=0;i<intervals.length;i++){
            time[intervals[i].start]++;
            time[intervals[i].end]--;
        }
        let max = time[0];
        for(let i=1;i<time.length;i++){
            time[i]=time[i-1]+time[i];
            max = Math.max(time[i],max);
        }
        return max;
    }
}
