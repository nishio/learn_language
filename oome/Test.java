/*
 * Copyright (c) 2004, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */
/**
 * This file derived from /openjdk/jdk/test/java/lang/management/MemoryMXBean/LowMemoryTest2.java
 * to demonstrate when OutOfMemoryError raise with large heap setting (such as -Xmx1G)
 * by NISHIO Hirokazu, 2013.
 */
public class Test extends ClassLoader{
    static int count = 0;
    Class loadNext() throws ClassNotFoundException {
        int body[] = {
            0xca, 0xfe, 0xba, 0xbe,  // CAFEBABE
            0x00, 0x00, 0x00, 0x30,  // version number: JDK 1.4.0

            0x00, 0x0a, // constant pool count: 10

            // constant 1
            0x0a, // tag: 10, Method reference
            0x00, 0x03, 0x00, 0x07, // constants 3 and 7
            // means (class, name&type)

            // constant 2
            0x07, // tag: 7, Class reference
            0x00, 0x08, // constant 8
            // means 'Test######'

            // constant 3
            0x07, // tag: 7, Class reference
            0x00, 0x09, // constant 9
            // means 'java/lang/Object'

            // constant 4
            0x01, // tag: 1, UTF-8 (Unicode) string
            0x00, 0x06, // length: 6
            0x3c, 0x69, 0x6e, 0x69, 0x74, 0x3e, // '<init>'

            // constant 5
            0x01, // tag: 1, UTF-8 (Unicode) string
            0x00, 0x03,  // length: 3
            0x28, 0x29, 0x56, // '()V'

            // constant 6
            0x01, // tag: 1, UTF-8 (Unicode) string
            0x00, 0x04,  // length: 4
            0x43, 0x6f, 0x64, 0x65, // 'Code'

            // constant 7
            0x0c, // tag: 12, Name and type descriptor
            0x00, 0x04, 0x00, 0x05, // constants 4 and 5
            // means ('<init>', '()V')

            // constant 8
            0x01, // tag: 1, UTF-8 (Unicode) string
            0x00, 0x0a, // length: 10
            0x54, 0x65, 0x73, 0x74, // T e s t
            0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, // Placeholders for 'Test######'

            // constant 9
            0x01, // tag: 1, UTF-8 (Unicode) string
            0x00, 0x10, // length: 16
            // 'java/lang/Object'
            0x6a, 0x61, 0x76, 0x61, 0x2f, 0x6c, 0x61, 0x6e,
            0x67, 0x2f, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74,

            0x00, 0x21, // access flags: synchronized + public
            0x00, 0x02, // this class, constant 2: 'Test######'
            0x00, 0x03, // super class, constant 3: 'java/lang/Object'

            0x00, 0x00, // interface count: 0

            0x00, 0x00, // field count: 0

            0x00, 0x01, // method count: 1

            // method 1
            0x00, 0x01, // access flags: public
            0x00, 0x04, // name: constant 4, '<init>'
            0x00, 0x05, // descripter: constant 5, '()V'
            0x00, 0x01, // attributes count: 1

            // attribute 1: Code
            0x00, 0x06, // attribute name: constant 6: 'Code'
            0x00, 0x00, 0x00, 0x11, // attribute length: 17
            0x00, 0x01, // max_stack: 1
            0x00, 0x01, // max_locals: 1
            0x00, 0x00, 0x00, 0x05, // code length: 5
            0x2a,             // 0:    aload_0
            0xb7, 0x00, 0x01, // 1:    invokespecial   #1; //Method java/lang/Object."<init>":()V
            0xb1,             // 4:    return
            0x00, 0x00, // exception table length: 0
            0x00, 0x00, // atrribute count: 0
            // end of method 1

            0x00, 0x00 // attribute count for class: 0
        };

        // generate name
        String name = String.format("Test%06d", count);

        // fill placeholder
        int denom = 100000;
        int c0 = 48;  // char code for '0'
        int placeholder = 55;
        for(int i=0; i < 6; i++){
            int v = count / denom % 10;
            body[placeholder + i] = c0 + v;
            denom /= 10;
        }

        // construct class file
        byte b[] = new byte[body.length];
        for(int i=0; i < body.length; i++){
            b[i] = (byte)body[i];
        }
        return defineClass(name, b, 0, b.length);

    }

    public static void main(String args[]) throws ClassNotFoundException{
        Test me = new Test();
        while(true){
            me.loadNext();
            count++;
            System.out.println(count);
        }
    }
}
