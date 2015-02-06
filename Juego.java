import java.util.Scanner;

public class Juego{
	public static void main(String args[]){
		char opcion;

		int casilla11 = 4;
		int casilla12 = 6;
		int casilla13 = 1;

		int casilla21 = 3;
		int casilla22 = 0;
		int casilla23 = 5;

		int casilla31 = 7;
		int casilla32 = 2;
		int casilla33 = 8;

		Scanner scanner=new Scanner(System.in);

		System.out.print("Menu: \n"+"Jugar (J)\n"+"Salir (E)\n");
		opcion=scanner.next().charAt(0);

		if(opcion=='j'){
			while(true){
			while(true){
				System.out.println("---------");
				System.out.println("|"+casilla11+"  "+casilla12+"  "+casilla13+"|\n");
				System.out.println("|"+casilla21+"  "+casilla22+"  "+casilla23+"|\n");
				System.out.println("|"+casilla31+"  "+casilla32+"  "+casilla33+"|");
				System.out.println("---------");

				System.out.print("Ingrese WASD (izquierda, arriba, abajo, derecha) o E para salir: ");
				opcion=scanner.next().charAt(0);

				if(opcion == 's'){
					if(casilla33 == 0){
					casilla33=casilla23;
					casilla23=0;
					break;
					}	
					if(casilla32 == 0){
					casilla32=casilla22;
					casilla22=0;
					break;
					}
					if(casilla31 == 0){
					casilla31=casilla21;
					casilla21=0;
					break;
					}		
					if(casilla23 == 0){
					casilla23=casilla13;
					casilla13=0;
					break;
					}
					if(casilla22 == 0){
					casilla22=casilla12;
					casilla12=0;
					break;
					}
					if(casilla21 == 0){
					casilla21=casilla11;
					casilla11=0;
					break;
					}
				}	
				if(opcion == 'w'){
					if(casilla13 == 0){
					casilla13=casilla23;
					casilla23=0;
					break;
					}
					if(casilla12 == 0){
					casilla12=casilla22;;
					casilla22=0;
					break;
					}
					if(casilla11 == 0){
					casilla11=casilla21;
					casilla21=0;
					break;
					}
					if(casilla23 == 0){
					casilla23=casilla33;
					casilla33=0;
					break;
					}
					if(casilla22 == 0){
					casilla22=casilla32;
					casilla32=0;
					break;
					}
					if(casilla21 == 0){
					casilla21=casilla31;
					casilla31=0;
					break;
					}					
				}

				if(opcion == 'd'){
					if(casilla13 == 0){
					casilla13=casilla12;
					casilla12=0;
					break;
					}
					if(casilla23 == 0){
					casilla23=casilla22;
					casilla22=0;
					break;
					}
					if(casilla33 == 0){
					casilla33=casilla32;
					casilla32=0;
					break;
					}
					if(casilla12 == 0){
					casilla12=casilla11;
					casilla11=0;
					break;
					}
					if(casilla22 == 0){
					casilla22=casilla21;
					casilla21=0;
					break;
					}
					if(casilla32 == 0){
					casilla32=casilla31;
					casilla31=0;
					break;
					}					
				}

				if(opcion == 'a'){
					if(casilla11 == 0){
					casilla11=casilla12;
					casilla12=0;
					break;
					}			
					if(casilla21 == 0){
					casilla21=casilla22;
					casilla22=0;
					break;
					}			
					if(casilla31 == 0){
					casilla31=casilla32;
					casilla32=0;
					break;
					}
					if(casilla12 == 0){
					casilla12=casilla13;
					casilla13=0;
					break;
					}
					if(casilla22 == 0){
					casilla22=casilla23;
					casilla23=0;
					break;
					}
					if(casilla32 == 0){
					casilla32=casilla33;
					casilla33=0;
					break;
					}		
				}
				if(opcion == 'e'){
					break;
				}	
			}
				if(opcion == 'e'){
					break;
				}	

				if(casilla11==1 && casilla12==2 && casilla13==3 && casilla21==4 && casilla22==5 && casilla23==6 && casilla31==7 && casilla32==8 && casilla33==0){
					System.out.print("Ganaste!");
					break;
				}	
		}	
		
		if(opcion=='e'){
			while(true){
			break;
			}	
		}

		}
	}
}