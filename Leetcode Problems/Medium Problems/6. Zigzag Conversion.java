public class Solution {
    public String convert(String s, int nRows) {

        if(nRows==1) return s;
        StringBuilder[] temp=new StringBuilder[nRows];
        for(int i=0;i<temp.length;i++) temp[i]=new StringBuilder();
        int idx=-1;
        int step=1;
        for(int i=0;i<s.length();i++){
            idx +=step;
            if(idx==nRows){
                idx=nRows-2;
                step=-1;
            }else if(idx==-1){
                idx=1;
                step=1;
            }
            temp[idx].append(s.charAt(i));
        }
        String ret="";
        for(int i=0;i<nRows;i++) ret+=temp[i].toString();
        return ret;
    }
}
