
public class Gem {
	
	private int stage;
	private int time;
	private int coin;
	private int jam;
	private int monster;

	public int getStage() {
		return stage;
	}

	public void setStage(int stage) {
		this.stage = stage;
	}

	public int getTime() {
		return time;
	}

	public void setTime(int time) {
		this.time = time;
	}

	public int getCoin() {
		return coin;
	}

	public void setCoin(int coin) {
		this.coin = coin;
	}

	public int getJam() {
		return jam;
	}

	public void setJam(int jam) {
		this.jam = jam;
	}

	public int getMonster() {
		return monster;
	}

	public void setMonster(int monster) {
		this.monster = monster;
	}
	
	public Gem(int stage, int time, int coin, int jam, int monster) {
		setStage(stage);
		setTime(time);
		setCoin(coin);
		setJam(jam);
		setMonster(monster);
	}
	
	public String stageInfo() {
		String stageInfo = String.format("%d-%d", stage / 10, stage % 10);
		return stageInfo;
	}
	
	public String timeInfo() {
		String calcTime = String.format("%d:%d", time / 100, time % 100);
		return calcTime;
	}
	
	public int inSecond() {
		int inSecond = ((time / 100) * 60) + (time % 100);
		return inSecond;
	}
	
	public double jps() {
		double jps = (double)jam / (double)inSecond();
		return jps;
	}
	
	public void gameInfo() {
		System.out.printf("Stage: %s%n", stageInfo());
		System.out.printf("Time: %s%n", timeInfo());
		System.out.printf("Coin: %s%n", coin);
		System.out.printf("Jam: %s%n", jam);
		System.out.printf("Monster: %s%n", monster);
		System.out.printf("Jams/Sec: %.2f", jps());
	}
}

























