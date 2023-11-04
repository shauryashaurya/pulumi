// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"regress-8403/mongodbatlas/internal"
)

func LookupCustomDbRoles(ctx *pulumi.Context, args *LookupCustomDbRolesArgs, opts ...pulumi.InvokeOption) (*LookupCustomDbRolesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCustomDbRolesResult
	err := ctx.Invoke("mongodbatlas::getCustomDbRoles", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCustomDbRolesArgs struct {
}

type LookupCustomDbRolesResult struct {
	Result *GetCustomDbRolesResult `pulumi:"result"`
}

func LookupCustomDbRolesOutput(ctx *pulumi.Context, args LookupCustomDbRolesOutputArgs, opts ...pulumi.InvokeOption) LookupCustomDbRolesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCustomDbRolesResult, error) {
			args := v.(LookupCustomDbRolesArgs)
			r, err := LookupCustomDbRoles(ctx, &args, opts...)
			var s LookupCustomDbRolesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCustomDbRolesResultOutput)
}

type LookupCustomDbRolesOutputArgs struct {
}

func (LookupCustomDbRolesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomDbRolesArgs)(nil)).Elem()
}

type LookupCustomDbRolesResultOutput struct{ *pulumi.OutputState }

func (LookupCustomDbRolesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomDbRolesResult)(nil)).Elem()
}

func (o LookupCustomDbRolesResultOutput) ToLookupCustomDbRolesResultOutput() LookupCustomDbRolesResultOutput {
	return o
}

func (o LookupCustomDbRolesResultOutput) ToLookupCustomDbRolesResultOutputWithContext(ctx context.Context) LookupCustomDbRolesResultOutput {
	return o
}

func (o LookupCustomDbRolesResultOutput) Result() GetCustomDbRolesResultPtrOutput {
	return o.ApplyT(func(v LookupCustomDbRolesResult) *GetCustomDbRolesResult { return v.Result }).(GetCustomDbRolesResultPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCustomDbRolesResultOutput{})
}
