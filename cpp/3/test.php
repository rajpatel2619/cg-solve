
class Foo{ 
    public 
        function makeFoo(callable $bar) :
        string { return "Hello ".$bar(); 
    } 
    }
    
    class Bar{ 
        public function 
        makeFooBar() :string { return (new Foo)->makeFoo([$this, 'makeBar']); } 
        private function makeBar() :
        string { return "World"; }
    }


echo (new Bar)->makeFooBar();