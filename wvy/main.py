import user
import wvy_server

def main():
    '''first_user = user.User()
    first_user_name = first_user.getName()
    one = user.Transform('testFunc', 'x')
    one_copy = user.Transform('testFunc', 'y')
    first_user.addTransform(one)
    first_user.addTransform(one_copy)
    if(first_user_name != 'test'):
        print('Test FAILED!')
        print(first_user_name)
    else:
        print('Success!')
    first_wave = user.Wave()
    first_wave.importFromFile('second_wave.csv')
    first_graph = user.Graph()
    first_graph.plotWave(first_wave)'''
    wvy_server.runServer(8910)

if __name__ == "__main__":
    main()
