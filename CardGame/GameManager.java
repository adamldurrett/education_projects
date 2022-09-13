public class GameManager{
	public static LinkedList players;


	public static void main(String [] args){
		System.out.println("Ready to play?");
		players = new LinkedList();
		playGame();
	}

	private static void playGame(){
		addPlayer("Player 1", false);
		addPlayer("Computer", true);
	}

	private static void addPlayer(String name, boolean cpu){
		players.add(new Player(name,cpu));
	}
}