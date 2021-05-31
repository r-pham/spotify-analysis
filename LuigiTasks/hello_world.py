# Example Usage: python hello_world.py HelloWorldTask --local-scheduler
import luigi

class HelloTask(luigi.Task) :
    def run(self):
        with open('hello.txt','w') as hello_file:
            hello_file.write('Hello')
            hello_file.close()

    def output(self) :
        return luigi.LocalTarget('hello.txt')

class WorldTask(luigi.Task) :

    def run(self):
        with open('world.txt','w') as world_file :
            world_file.write('World')
            world_file.close()

    def output(self) :
        return luigi.LocalTarget('world.txt')

class HelloWorldTask(luigi.Task) :

    def requires(self) :
        return [HelloTask(), WorldTask()]

    def run(self):
        with open('hello.txt','r') as hello_file :
            hello = hello_file.read()

        with open('world.txt','r') as world_file :
            world = world_file.read()   

        with open('helloworld.txt','w') as helloworld_file :
            helloworld_file.write(hello)
            helloworld_file.write(world)
            helloworld_file.close()

    def output(self) :
        return luigi.LocalTarget('helloworld.txt')

if __name__ == '__main__':
    luigi.run()