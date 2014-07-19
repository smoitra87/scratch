package com.deepmoitra;

import com.deepmoitra.Util;
import com.google.common.base.Optional;


public class Main {


    public static void main(String[] args) {
        System.out.println(Util.getHostname());
        Optional<Foo> possible = Optional.absent();
        if(!possible.isPresent()) {
            System.out.println("Object not found");
        } 


        Foo foo = new Foo("bar");
        possible = Optional.of(foo);
        if(!possible.isPresent()) {
            System.out.println("Object not found");
        } else {
            System.out.println(possible.get().name);
        }

    }

   

    private static class Foo {
        public String name;
        public Foo(String _) {
            name = _;
        }

    }

}
