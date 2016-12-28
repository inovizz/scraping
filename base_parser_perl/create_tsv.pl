#!/usr/bin/perl

use Data::Dumper qw(Dumper);

open (MYFILE, "<", $ARGV[0]);
open (OUTFILE, ">", $ARGV[1]);

@myfile =  <MYFILE>;
close (MYFILE);

my %header;
for( $i = 0; $i < $#myfile; $i++ )
{
	if( $myfile[$i] =~ /-----/ )
	{
		next;
	}
	else
	{
		$tag = $myfile[$i];
		$tag =~ s/(.*?)\s+::\s+.*/\1/;
		chomp( $tag );
		if(!defined $header{$tag})
		{
			$header{$tag} = 'TRUE';
		}
		else
		{
			next;
		}
	}
}

foreach $key ( keys %header )
{
	print OUTFILE $key . "\t";
	
}

my %final;
for ($i=0; $i<$#myfile; $i++)
{
	my $tag = $myfile[$i];
	my $value = $myfile[$i];
	chomp( $tag );
	chomp(  $value );
	if($tag =~ /\s+::\s+/is)
	{
		$tag =~ s/(.*?)\s+::\s+.*/\1/;
		$value =~ s/.*?::\s+(.*)/\1/;
		$final{$tag} = $value;
	}
	
	if( $tag =~ /------/ or ($i+1 == $#myfile))
	{
		my $output = "";
		foreach my $key ( keys %header )
		{	
			if($final{$key} eq 'TRUE')
			{
				$output = $output .  "\t";
			}
			else
			{
				$output = $output . $final{$key} . "\t";
			}
		}
		$output = $output .  $url;
		print OUTFILE "$output\n";
		%final = ();
	}
}

close (OUTFILE);
