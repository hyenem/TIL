package SWEA_13072_병사관리;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class UserSolution
{
	ArrayList<int[]> list = new ArrayList<>();
	Map<Integer, Integer> map = new HashMap<>();
	ArrayList<ArrayList<Integer>> team = new ArrayList<>();
	int index = 0;
	
	public void init()
	{
		list.clear();
		map.clear();
		index = 0;
		team.clear();
		for(int i = 0; i<5; i++) {
			team.add(new ArrayList<Integer>());
		}
	}
	
	public void hire(int mID, int mTeam, int mScore)
	{
		list.add(new int[]{mID,mTeam,mScore});
		map.put(mID, index);
		team.get(mTeam-1).add(index++);
	}
	
	public void fire(int mID)
	{
		list.get(map.get(mID))[1]=-1;
		map.remove(mID);
	}

	public void updateSoldier(int mID, int mScore)
	{
		list.get(map.get(mID))[2] = mScore;
	}

	public void updateTeam(int mTeam, int mChangeScore)
	{
		for(int i = 0; i<team.get(mTeam-1).size(); i++) {
			int[] thisSolder = list.get(team.get(mTeam-1).get(i));
			if(thisSolder[2]+mChangeScore>5) thisSolder[2]=5;
			else if(thisSolder[2]+mChangeScore<1) thisSolder[2]=1;
			else thisSolder[2] += mChangeScore;
		}
	}
	
	public int bestSoldier(int mTeam)
	{	
		int[] maxSolder= {-1,-1,-1};
		for(int i = 0; i<team.get(mTeam-1).size(); i++) {
			int[] thisSolder = list.get(team.get(mTeam-1).get(i));
			if(thisSolder[1]==mTeam) {
				if(thisSolder[2]>maxSolder[2]) maxSolder = thisSolder;
				else if(thisSolder[2]==maxSolder[2]) {
					if(thisSolder[0]>maxSolder[0]) maxSolder=thisSolder;
				}
			}
		}
		return maxSolder[0];
	}
}