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
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        intervals.sort((a,b)=>a.start-b.start);
        if(intervals.length<=1) return true;
        let end = intervals[0].end;
        for(let i=1;i<intervals.length;i++){
            const interval  = intervals[i];
            if(interval.start<end){
                return false;
            }
            end = interval.end;
        }
        return true;
    }
}
