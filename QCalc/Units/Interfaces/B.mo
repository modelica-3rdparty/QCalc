within QCalc.Units.Interfaces;
operator record B "bel (B) (in terms of power ratio, not amplitude ratio)"
  extends LambdaUnit(redeclare type Quantity = Q.Number);

  operator '*' "Multiplication is overloaded to map a number to a quantity"
    function num2qty "Convert a number to a quantity"

      input Real n "Number";
      input B selfDummy "2nd argument is the unit itself; contains no data";
      output Quantity q "Quantity";

    algorithm
      q := 10^n;
      annotation (Inline=true, inverse(n='/'.qty2num(q, selfDummy)));
    end num2qty;
  end '*';

  operator '/' "Division is overloaded to map a quantity to a number"

    function qty2num "Convert a quantity to a number"

      input Quantity q "Quantity";
      input B selfDummy "2nd argument is the unit itself; contains no data";
      output Real n "Number";

    algorithm
      n := log10(q);
      annotation (Inline=true, inverse(q='*'.num2qty(n, selfDummy)));
    end qty2num;
  end '/';
end B;
