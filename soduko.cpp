#include<iostream>
#include<vector>




std::pair<int,int> find_empty(int *board, int dim1, int dim2){

    for(int i=0;i<dim1;i++){
        for(int j=0;j<dim2;j++){
            if( board[i*dim2+j]==0){
                return {i,j};
            }
        }
    }
    return{-1,-1};
}


bool promising(int board[][9], int i,int j){

    //cehck for row
    for (uint x = 0; x < j+1; x++)
    {
        for (uint y = 0; y < j+1; y++)
        {
            if((board[x][j] == board[y][j]) && (x != y) && board[x][j]){
                return false;
            }
        }   
    }
    

    //check for column
      for (uint x = 0; x < i+1; x++)
    {
        for (uint y = 0; y < i+1; y++)
        {
            if((board[i][x] == board[i][y]) && (x != y) &&(board[i][x]!=0)){
                return false;
            }
        }   
    }

    // check for 3*3 square


    return true;
}


void print_board(int *board,int dim1,int dim2){

    for(int i = 0; i<dim1;i++){
        for(int j=0;j<dim2;j++){
            std::cout<< board[i*dim2+j] <<" ";
        }
        std::cout<<std::endl;
    }

}

int main(int argc,char *argv[]){

// in case of dynamic 2d array
    
    // int **board = new int*[10];

    // std::cout<< "this is argv "<<argv[1]<<std::endl;
    // for(int i =0 ; i<10;i++)
    //     board[i] = new int [atoi(argv[1])]; // atoi cast a string to int, int 64 bit machin you cant cast int to char becuase int is 8 byte and char is 4 byte

    // for (int i = 0;i<10;i++)
    //     for(int j=0;j<10;j++)
    //         board[i][j] = i;


    // for (int i = 0;i<10;i++){
    //     for(int j=0;j<10;j++){
    //         std::cout<<board[i][j]<<" ";
    //     }
    //     std::cout<< std::endl;
    // }

    int board[9][9] = {
                        {7,8,0,4,0,0,1,2,0},
                        {6,0,0,0,7,5,0,0,9},
                        {0,0,0,6,0,1,0,7,8},
                        {0,0,7,0,4,0,2,6,0},
                        {0,0,1,0,5,0,9,3,0},
                        {9,0,4,0,6,0,0,0,5},
                        {0,7,0,3,0,0,0,1,2},
                        {1,2,0,0,0,7,4,0,0},
                        {0,4,9,2,0,6,0,0,7}
                      }; // game board 

    print_board(board[0],9,9);
    auto [a,b] = find_empty(board[0],9,9);
    std::cout<<a<<" "<<b <<std::endl;
    std::cout<<"promising is :"<<promising(board,0,7);


    

    std::cin.get();
}