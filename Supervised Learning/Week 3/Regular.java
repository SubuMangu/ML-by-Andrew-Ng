public class Regular{
    public boolean match(char a,char b){
        return a==b || (a=='.'||b=='.');
    }

    public boolean isMatch(String s, String p) {
        if (s.isEmpty() && p.isEmpty()) return true;
        if (p.isEmpty()||s.isEmpty()) return false;
        int l1=s.length()-1;
        int l2=p.length()-1;
        if(p.charAt(l2)=='*')
            return isMatch(s,p.substring(0,l2-1))|| (match(s.charAt(l1),p.charAt(l2-1)) && isMatch(s.substring(0,l1),p));
        else return match(s.charAt(l1),p.charAt(l2)) && isMatch(s.substring(0,l1),p.substring(0,l2));
    }
    public static void main(String[] args) {
        String a="aab.sd.";
        String b="aab.*";
        Regular r=new Regular();
        if(r.isMatch(a,b))System.out.println("a and b match");
        else System.out.println("a and b dont match");
    }
    
}